import React from 'react'
import * as C from '../../styles/components'
import * as S from './AuthorizationStyles'
import { SubmitHandler, useForm } from 'react-hook-form'
import userApi from '../../services/UserServise'
import { IAuthData } from '../../modules/IAuth'
const Authorization = () => {

  const [fetchAuth, {data: auth, error}] = userApi.useFetchAuthMutation()
  console.log(auth?.token)

  const {
    register,
    formState: { errors, isValid},
    handleSubmit
  } = useForm<IAuthData>({mode: 'onBlur'})

  const onSubmit: SubmitHandler<IAuthData> = async (data) => {
    await fetchAuth(data)
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
              {(errors?.password || error) && <p>{errors?.password?.message || 'Ошибка от апи'}</p>}
              <S.Button disabled={!isValid}>Продолжить</S.Button>
            </S.Form>
        </C.Container>
    </div>
  )
}

export default Authorization
