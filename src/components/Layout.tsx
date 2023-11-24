import React from 'react'
import { Outlet } from 'react-router-dom'
import styled, { ThemeProvider } from 'styled-components'
import * as C from "../styles/components"
import GlobalStyles from "../styles/global"
import Header from './header/Header'
import { baseTheme } from '../styles/theme'

const Layout = () => {
    return (
        <ThemeProvider theme={baseTheme}>
            <Wrapper>
                <Header/>
                <Main>
                    <C.Container>
                        <Outlet />
                    </C.Container>
                </Main>
                <GlobalStyles />
            </Wrapper>
        </ThemeProvider>
    )
}

export default Layout

const Wrapper = styled.div`
  width: 390px;
  margin: 0 auto;
`
const Main = styled.div`
  padding-top: 64px;
`