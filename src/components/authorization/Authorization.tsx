import React from 'react'
import * as C from '../../styles/components'
import * as S from './AuthorizationStyles'
import { SubmitHandler, useForm } from 'react-hook-form'
const Authorization = () => {
  interface AuthForm {
    login: string,
    password: string
  }

  const {
    register,
    formState: { errors, isValid},
    handleSubmit
  } = useForm<AuthForm>({mode: 'onBlur'})

  const onSubmit: SubmitHandler<AuthForm> = (data) => {

  }

  return (
    <div>
        <C.Container>
            <p>Войти</p>
            <S.Form onSubmit={handleSubmit(onSubmit)}>
              <S.Label htmlFor="login">Логин</S.Label>
              <S.Input id='login' {...register('login', {required: 'Поле обязательно к заполнению'})}/>
              {errors?.login && <p>{errors?.login?.message}</p>}
              <S.Label htmlFor="password">Пароль</S.Label>
              <S.Input id='password' type="password" {...register('password', {required: 'Поле обязательно к заполнению'})} />
              {errors?.password && <p>{errors?.password?.message}</p>}
              <S.Button disabled={!isValid}>Продолжить</S.Button>
            </S.Form>
        </C.Container>
    </div>
  )
}

export default Authorization
