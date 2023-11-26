import React, { FC } from 'react'
import TableHeader from './CTableHeader'
import { styled } from 'styled-components'
import TableRow from './CTableRow'
import candidateApi from '../../../services/CandidateService'
import { useParams } from 'react-router-dom'

const CTable: FC = () => {
    const {id} = useParams()
    const {data} = candidateApi.useFetchCandidatesQuery({limit: 10, id: id ? id : ''})
    const candidates = data?.results

    return (
        <TableContainer>
            <Table>
                <TableHeader />
                <tbody>
                    {candidates &&candidates.map(candidate => <TableRow key={candidate.candidatId} candidate={candidate} />)}
                </tbody>
            </Table>
        </TableContainer>

  )
}

export default CTable

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
