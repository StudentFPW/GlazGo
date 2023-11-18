import React, { FC, useEffect } from 'react'
import * as C from '../../styles/components'
import * as S from './AuthorizationStyles'
import { SubmitHandler, useForm } from 'react-hook-form'
import userApi from '../../services/UserService'
import { IAuthData } from '../../modules/IAuth'
import { useNavigate } from 'react-router-dom'
const Authorization:FC = () => {

  // const [fetchReg, {data: auth, error}] = userApi.useFetchRegMutation()
  const [fetchAuth, { data: auth, error, isSuccess }] = userApi.useFetchAuthMutation()

  if (auth?.accessToken) localStorage.setItem('accessToken', auth?.accessToken)

  const navigate = useNavigate()

  useEffect(() => {
    if (isSuccess) navigate('/vacancies')
  }, [isSuccess, navigate])

  const {
    register,
    formState: { errors, isValid},
    handleSubmit
  } = useForm<IAuthData>({mode: 'onBlur'})

  // const onSubmit: SubmitHandler<IAuthData> = async (data) => {
  //   await fetchReg(data)
  // }
  const onSubmit: SubmitHandler<IAuthData> = async (data) => {
    await fetchAuth(data)
  }

  return (
    <div>
      <C.H2>Войти</C.H2>
      <S.Form onSubmit={handleSubmit(onSubmit)}>
        <S.Label htmlFor="login">Логин</S.Label>
        <S.Input id='login' {...register('email', {required: 'Поле обязательно к заполнению'})}/>
        {errors?.email && <p>{errors?.email?.message}</p>}
        <S.Label htmlFor="password">Пароль</S.Label>
        <S.Input id='password' type="password" {...register('password', {required: 'Поле обязательно к заполнению'})} />
        {(errors?.password || error) && <p>{errors?.password?.message || 'Ошибка от апи'}</p>}
        <C.FButton disabled={!isValid}>Продолжить</C.FButton>
      </S.Form>
    </div>
  )
}

export default Authorization
