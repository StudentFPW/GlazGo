import React, { FC } from 'react'
import TableHeader from './CTableHeader'
import { styled } from 'styled-components'
import data from '../../../candidates.json'
import TableRow from './CTableRow'

const CTable: FC = () => {

    const candidates = data
    return (
        <TableContainer>
            <Table>
                <TableHeader />
                <tbody>
                    {candidates.map(candidate => <TableRow key={candidate.id} candidateItem={candidate} />)}
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
