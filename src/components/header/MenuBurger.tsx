import React, { FC, useState } from 'react'
import { NavLink } from 'react-router-dom'
import { css, styled } from 'styled-components'
import Burger from '../../images/icons/Burger'
import Close from '../../images/icons/Close'
import Logo from '../../images/icons/Logo'
import * as C from '../../styles/components'

const MenuBurger: FC = () => {
    const [nav, setNav] = useState(false)

    const toggleNav = () => {
        setNav(!nav);
    }

    return (
        <div>
            <div>
                <Icons>
                    <Btn onClick={toggleNav}>
                        {nav ? <SClose><Close/></SClose> : <Burger/>}
                    </Btn>
                    <SLogo>
                        <Logo/>
                    </SLogo>
                </Icons>
                {nav &&
                    <NavWrapper>
                        <C.Container>
                            <nav>
                                <ul>
                                    <li><NavLink to="/authorization" onClick={toggleNav}>Авторизация</NavLink></li>
                                    <li><NavLink to="/vacancies" onClick={toggleNav}>Вакансии</NavLink></li>
                                    <li><NavLink to="/candidates" onClick={toggleNav}>Кандидаты</NavLink></li>
                                    <li><NavLink to="/candidate" onClick={toggleNav}>Кандидат</NavLink></li>
                                    <li><NavLink to="/vacancy-closed" onClick={toggleNav}>Вакансия закрыта</NavLink></li>
                                    <li><NavLink to="/chat" onClick={toggleNav}>Чат</NavLink></li>
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

const Icons = styled.div`
    display: flex;
    column-gap: 14px;
    align-items: center;
`
const Btn = styled.div`
    z-index: ${({ theme }) => theme.order.burger};
`
const whiteSvgIcon = css`
    g {
        path {
            fill:  ${({ theme }) => theme.colors.white};
        }
    }
`
const SClose = styled.div`
    ${whiteSvgIcon}
`
const SLogo = styled.div`
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
