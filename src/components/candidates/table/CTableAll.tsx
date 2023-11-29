import React, { FC, useEffect } from 'react'
import TableHeader from './CTableHeader'
import { styled } from 'styled-components'
import TableRow from './CTableRow'
import candidateApi from '../../../services/CandidateService'
import { useParams } from 'react-router-dom'
import { useAppSelector } from '../../../hooks/redux'

const CTableAll: FC = () => {
    const {data} = candidateApi.useFetchAllCandidatesQuery()
    const candidates = data?.results
    console.log(candidates)
    const url = data?.next.slice(data?.next.indexOf('?'))
    console.log(url)
    const isNext = useAppSelector(state => state.pagination.isNext)
    useEffect(() => {
        if (isNext) {
            const {data: datas} = candidateApi.useFetchLimitCandidatesQuery(url ? url : '')
            console.log(datas)
            console.log('datas')
        }
    }, [isNext])
    // if (isNext) {
    //     const {data: datas} = candidateApi.useFetchLimitCandidatesQuery(url ? url : '')
    //     console.log(datas)
    //     console.log('datas')
    // }


    return (
        <TableContainer>
            <Table>
                <TableHeader />
                <tbody>
                    {candidates &&candidates.map(candidate => <TableRow key={candidate.candidatId.id} candidate={candidate} />)}
                </tbody>
            </Table>
        </TableContainer>

  )
}

export default CTableAll

const TableContainer = styled.div`
    max-width: 100%;
    overflow-x: auto;
`

const Table = styled.table`
    table-layout: fixed;
    width: 100%;
    max-width: 600px;
    border-collapse: collapse;
    border: 1px solid #D7D7D7;
    margin: 20px 0;
`
