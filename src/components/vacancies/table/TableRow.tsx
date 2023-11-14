import React, { FC } from 'react'
import { IVacancyItem } from '../../../modules/IVacancyItem'
import styled from 'styled-components'

interface VacancyItemProps {
    vacancyItem: IVacancyItem
}
const TableRow: FC<VacancyItemProps> = ({vacancyItem}) => {
    const {vacancy, status, city, salary, id} = vacancyItem

    return (
        <tr>
            <Td>{vacancy}</Td>
            <Td>{status}</Td>
            <Td>{city}</Td>
            <Td>{salary}</Td>
            <Td>{id}</Td>
        </tr>
    )
}

export default TableRow

const Td = styled.td`
    padding: 10px 16px;
    white-space: nowrap;
    overflow: hidden;
    font-size: 14px;
`
