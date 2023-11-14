import React, { FC } from 'react'
import * as C from '../../styles/components'
import * as S from './AuthorizationStyles'
import { SubmitHandler, useForm } from 'react-hook-form'
import userApi from '../../services/UserService'
import { IAuthData } from '../../modules/IAuth'
const Authorization:FC = () => {

  // const [fetchReg, {data: auth, error}] = userApi.useFetchRegMutation()
  const [fetchAuth, {data: auth, error}] = userApi.useFetchAuthMutation()

  if (auth?.accessToken) localStorage.setItem('accessToken', auth?.accessToken)

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
      <p>Войти</p>
      <S.Form onSubmit={handleSubmit(onSubmit)}>
        <S.Label htmlFor="login">Логин</S.Label>
        <S.Input id='login' {...register('email', {required: 'Поле обязательно к заполнению'})}/>
        {errors?.email && <p>{errors?.email?.message}</p>}
        <S.Label htmlFor="password">Пароль</S.Label>
        <S.Input id='password' type="password" {...register('password', {required: 'Поле обязательно к заполнению'})} />
        {(errors?.password || error) && <p>{errors?.password?.message || 'Ошибка от апи'}</p>}
        <S.Button disabled={!isValid}>Продолжить</S.Button>
      </S.Form>
    </div>
  )
}

export default Authorization
