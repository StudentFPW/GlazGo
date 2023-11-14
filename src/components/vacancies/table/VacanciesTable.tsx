import React, { FC } from 'react'
import TableHeader from './TableHeader'
import { styled } from 'styled-components'
import data from '../../../stubbing.json'
import TableRow from './TableRow'

const VacanciesTable: FC = () => {

    const vacansies = data
    return (
        <TableContainer>
            <Table>
                <TableHeader />
                <tbody>
                    {vacansies.map(vacancy => <TableRow key={vacancy.id} vacancyItem={vacancy} />)}
                </tbody>
            </Table>
        </TableContainer>

  )
}

export default VacanciesTable

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
