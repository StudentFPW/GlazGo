import React from 'react'
import { css, styled } from 'styled-components'

const Options = () => {
    return (
        <div>
            <BtnContainer>
                <Button>Добавить</Button>
                <Button>Фильтры</Button>
            </BtnContainer>
        </div>
    )
}

export default Options

const BtnContainer = styled.div`
    display: flex;
    column-gap: 12px;
`
const Button = styled.button`
    padding: 10px 12px;
    border-radius: 6px;
    border: 0.5px solid #BEBEBE;
    background: #FFF;
    box-shadow: 0px 4px 4px 0px rgba(17, 30, 62, 0.06);
    font-size: 16px;
    font-weight: 500;
    line-height: 20px; /* 125% */
    letter-spacing: -0.08px;
    color: #121212;
`
