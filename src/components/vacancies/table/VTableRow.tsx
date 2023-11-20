import React, { FC } from 'react'
import styled from 'styled-components'
import { IVacancyItem } from '../../../modules/IVacancyItem'
import vacancyApi from '../../../services/VacancyService'

interface VacancyItemProps {
    vacancyItem: IVacancyItem
}

const VTableRow: FC<VacancyItemProps> = ({vacancyItem}) => {

    const {vacancy, status, city, salary, id} = vacancyItem

    const [getVacancy, {}] = vacancyApi.useGetVacancyQuery(id)

    const handleVacancyClick = () => {


    }

    return (
        <tr>
            <Td onClick={handleVacancyClick}>{vacancy}</Td>
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
