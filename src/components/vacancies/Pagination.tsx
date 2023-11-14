import React from 'react'
import styled from 'styled-components'
import ArrowLeft from '../../images/icons/ArrowLeft'
import ArrowRight from '../../images/icons/ArrowRight'


const Pagination = () => {
    return (
        <PContainer>
            <p>1 - 7 из 50 страниц</p>
            <Arrows>
                <Button><ArrowLeft /></Button>
                <Button><ArrowRight /></Button>
            </Arrows>
        </PContainer>
    )
}

export default Pagination

const PContainer = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 16px;
    font-weight: 400;
    line-height: 20px; /* 125% */
    letter-spacing: -0.08px;
`
const Arrows = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;
    column-gap: 16px;
`
const Button = styled.button`
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 6px;
    border: 0.5px solid #BEBEBE;
    background: #FFF;
    box-shadow: 0px 4px 4px 0px rgba(17, 30, 62, 0.06);
`