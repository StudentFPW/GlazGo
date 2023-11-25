import React, { FC, useEffect } from 'react'
import * as C from '../../styles/components'
import * as S from './AuthorizationStyles'
import { SubmitHandler, useForm } from 'react-hook-form'
import { IAuthData } from '../../modules/IAuth'
import { useNavigate } from 'react-router-dom'
import { useAppDispatch } from '../../hooks/redux'
import { setAuth } from '../../store/redusers/authSlice'
import authApi from '../../services/AuthService'

const Authorization:FC = () => {

  const [login, { data, error, isSuccess }] = authApi.useLoginMutation()
  const dispatch = useAppDispatch()

  if (data) {
    localStorage.setItem('accessToken', data.access)
    localStorage.setItem('role', data.user.role.toString())
    dispatch(setAuth())
  }

  const navigate = useNavigate()

  const handleGoToReg = () => navigate('/registration')

  useEffect(() => {
    if (isSuccess) navigate('/vacancies')
  }, [isSuccess, navigate])

  const {
    register,
    formState: { errors, isValid},
    handleSubmit
  } = useForm<IAuthData>({mode: 'onBlur'})

  const onSubmit: SubmitHandler<IAuthData> = async (data) => {
    await login(data)
  }

  return (
    <div>
      <S.Title>
        <C.H2>Войти</C.H2>
        <div onClick={handleGoToReg}>Зарегистрироваться</div>
      </S.Title>
      <S.Form onSubmit={handleSubmit(onSubmit)}>
        <S.Label htmlFor="username">Логин</S.Label>
        <S.Input id='username' {...register('username', {required: 'Поле обязательно к заполнению'})}/>
        {errors?.username && <p>{errors?.username?.message}</p>}
        <S.Label htmlFor="password">Пароль</S.Label>
        <S.Input id='password' type="password" {...register('password', {required: 'Поле обязательно к заполнению'})} />
        {(errors?.password || error) && <p>{errors?.password?.message || 'Ошибка от апи'}</p>}
        <C.FButton disabled={!isValid}>Продолжить</C.FButton>
      </S.Form>
    </div>
  )
}

export default Authorization
