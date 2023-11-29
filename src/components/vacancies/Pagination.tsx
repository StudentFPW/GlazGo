import React, { FC, useEffect } from 'react'
import styled from 'styled-components'
import ArrowLeft from '../../images/icons/arrow-left.svg'
import ArrowRight from '../../images/icons/arrow-right.svg'
import * as C from '../../styles/components'
import { ICandidatesResponseData } from '../../modules/ICandidate'
import { IPagination } from '../../modules/IPagination'
import candidateApi from '../../services/CandidateService'
import { useAppDispatch } from '../../hooks/redux'
import { setNext } from '../../store/redusers/paginationSlice'

const Pagination: FC<IPagination> = ({count, next, previous}) => {
    // let url = ''
    // // let data

    // if (next) {
    //     return url = next.slice(next.indexOf('?'))
    // }

    // const handleNextPage = () => {
    //     if (next.includes('api-c-p')) {
    //         const {data} = candidateApi.useFetchLimitCandidatesQuery(url)
    //     }
    // }

    const dispatch = useAppDispatch()
    const handleQuery = () => {
        dispatch(setNext())
    }
    // useEffect(() => {
    //     handleQuery()
    //   }, [])

    return (
        <PContainer>
            <p>{count > 10 ? 10 : count} из {count}</p>
            <Arrows>
                <C.NButton><ArrowLeft/></C.NButton>
                <C.NButton onClick={handleQuery}><ArrowRight/></C.NButton>
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