import React from 'react'
import notFound from '../images/not-found.svg'
import NotFound from '../images/NotFound'
import { styled } from 'styled-components'
import * as C from '../styles/components'

const NotFoundPage = () => {
    return (
        <Container>
            <C.H1>Страница не найдена</C.H1>
            <Img src={notFound} alt="not found" />
        </Container>
    )
}

export default NotFoundPage

const Container = styled.div`
    height: 100svh;
    display: flex;
    flex-direction: column;
    justify-content: center;
`
const Title = styled.h1`
    margin: 15px 0;
`
const Img = styled.img`
    width: 100%;
`