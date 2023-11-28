import React from 'react'
import * as C from '../styles/components'
import Success from '../images/success.svg'
import { styled } from 'styled-components'

const VacancyClosed = () => {
    return (
        <div>
            <ImgWrapper>
                <Success />
             </ImgWrapper>
            <C.H1>Поздравляем! Вакансия Директор закрыта</C.H1>
            <div>Вернуться к списку вакансий</div>
        </div>
    )
}

export default VacancyClosed

const ImgWrapper = styled.div`
    display: flex;
    justify-content: center;
    svg {
        width: 213px;
        height: 293px;
    }
`