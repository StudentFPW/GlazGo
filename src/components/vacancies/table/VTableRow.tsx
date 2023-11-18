import React, { FC } from 'react'
import { IVacancyItem } from '../../../modules/IVacancyItem'
import styled from 'styled-components'

interface VacancyItemProps {
    vacancyItem: IVacancyItem
}
const VTableRow: FC<VacancyItemProps> = ({vacancyItem}) => {
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

export default VTableRow

const Td = styled.td`
    padding: 10px 16px;
    white-space: nowrap;
    overflow: hidden;
    font-size: 14px;
`
