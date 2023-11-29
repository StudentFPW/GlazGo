import React from 'react'
import styled from 'styled-components'
import ArrowLeft from '../../images/icons/arrow-left.svg'
import ArrowRight from '../../images/icons/arrow-right.svg'
import * as C from '../../styles/components'

const Pagination = () => {
    return (
        <PContainer>
            <p>1 - 7 из 50 страниц</p>
            <Arrows>
                <C.NButton><ArrowLeft/></C.NButton>
                <C.NButton><ArrowRight /></C.NButton>
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
    margin-top: 24px;
`
const Arrows = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;
    column-gap: 16px;
`