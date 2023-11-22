import React, { FC } from 'react'
import TableHeader from './VTableHeader'
import { styled } from 'styled-components'
import VTableRow from './VTableRow'
import vacancyApi from '../../../services/VacancyService'

const VTable: FC = () => {
    const {data: vacancies} = vacancyApi.useGetVacanciesQuery(10)

    return (
        <TableContainer>
            <Table>
                <TableHeader />
                <tbody>
                    {vacancies && vacancies.map(vacancy => <VTableRow key={vacancy.id} vacancy={vacancy} />)}
                </tbody>
            </Table>
        </TableContainer>
    )
}

export default VTable

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
`
