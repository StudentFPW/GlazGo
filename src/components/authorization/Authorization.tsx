import React from 'react'
import * as C from '../../styles/components'
import * as S from './Styles'
const Authorization = () => {
  return (
    <div>
        <C.Container>
            <p>Войти</p>
            <S.Form action="">
              <S.Label htmlFor="login">Логин</S.Label>
              <S.Input type="text" id='login'/>
              <S.Label htmlFor="password">Пароль</S.Label>
              <S.Input type="text" id='password' />
              <S.Button>Продолжить</S.Button>
            </S.Form>
        </C.Container>
    </div>
  )
}

export default Authorization
