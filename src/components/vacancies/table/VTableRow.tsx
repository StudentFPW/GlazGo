import React, { FC } from 'react'
import styled from 'styled-components'
import { IVacancy } from '../../../modules/IVacancy'
import { Link } from 'react-router-dom'

interface VacancyItemProps {
    vacancy: IVacancy
}

const VTableRow: FC<VacancyItemProps> = ({vacancy}) => {

    const {nameVacancy, status, city, salary, id} = vacancy

    return (
        <tr>
            <Link to={`/vacancy/${id}`}>
                <Td>{nameVacancy}</Td>
            </Link>
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
