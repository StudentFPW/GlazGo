import React, { FC, useState } from 'react'
import { NavLink, useNavigate } from 'react-router-dom'
import { css, styled } from 'styled-components'
import Burger from '../../images/icons/burger.svg'
import Close from '../../images/icons/close.svg'
import Logo from '../../images/icons/logo.svg'
import * as C from '../../styles/components'
import { useAppDispatch, useAppSelector } from '../../hooks/redux'
import authApi from '../../services/AuthService'
import { logout } from '../../store/redusers/authSlice'

const MenuBurger: FC = () => {
    const [nav, setNav] = useState(false)
    const navigate = useNavigate()
    const handleGoToAuth = () => navigate('/authorization')
    const handleToggleNav = () => setNav(!nav)
    const handleGoToHome = () => navigate('/')
    const isAuth = useAppSelector(state => state.auth.isAuth)
    const dispatch = useAppDispatch()
    const [logoutUser] = authApi.useLogoutMutation()
    // const {} = authApi.useLogoutQuery({})
    const handleLogOut = async () => {
        await logoutUser({})
        dispatch(logout())
    }

    let content

    if (isAuth) {
        content = <div onClick={handleLogOut}>Выйти</div>
    } else {
        content = <div onClick={handleGoToAuth}>Войти</div>
    }

    return (
        <div>
            <div>
                <Header>
                    <Icons>
                        <Btn onClick={handleToggleNav}>
                            {nav ? <SClose><Close/></SClose> : <Burger/>}
                        </Btn>
                        <SLogo onClick={handleGoToHome}>
                            <Logo />
                        </SLogo>
                    </Icons>
                    {content}
                </Header>
                {nav &&
                    <NavWrapper>
                        <C.Container>
                            <nav>
                                <ul>
                                    <li><NavLink to="/vacancies" onClick={handleToggleNav}>Вакансии</NavLink></li>
                                    <li><NavLink to="/vacancy-closed" onClick={handleToggleNav}>Вакансия закрыта</NavLink></li>
                                    <li><NavLink to="/chat" onClick={handleToggleNav}>Чат</NavLink></li>
                                </ul>
                            </nav>
                        </C.Container>
                    </NavWrapper>
                }
            </div>
        </div>
    )
}

export default MenuBurger

const Header = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: ${({ theme }) => theme.colors.white};
`
const Icons = styled.div`
    display: flex;
    column-gap: 14px;
    align-items: center;
`
const Btn = styled.div`
    z-index: ${({ theme }) => theme.order.burger};
`
const whiteSvgIcon = css`
    path {
        fill:  ${({ theme }) => theme.colors.white};
    }
`
const SClose = styled.div`
    ${whiteSvgIcon}
`
const SLogo = styled.div`
    height: 18px;
    svg {
        width: 78px;
        height: 18px;
        ${whiteSvgIcon}
    }
`
const NavWrapper = styled.div`
    color: ${({ theme }) => theme.colors.white};
    position: fixed;
    left: 0;
    width: 100%;
    height: 100svh;
    background-color: ${({ theme }) => theme.colors.primary};
    z-index: ${({ theme }) => theme.order.header};
    top: 64px;
    transition: top 2s;
        ul {
        display: flex;
        flex-direction: column;
        row-gap: 20px;
        margin: 24px 0;
    }
`
