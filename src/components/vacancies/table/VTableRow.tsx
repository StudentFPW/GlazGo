import React, { FC } from 'react'
import styled from 'styled-components'
import { IVacancy } from '../../../modules/IVacancy'
import { useNavigate } from 'react-router-dom'

interface VacancyItemProps {
    vacancy: IVacancy
}

const VTableRow: FC<VacancyItemProps> = ({vacancy}) => {

    const {nameVacancy, statusVacancy, region, salary, id} = vacancy

    const navigate = useNavigate()
    const handleGoToVacancy = () => navigate(`/vacancy/${id}`)

    return (
        <tr>
            <Td onClick={handleGoToVacancy}>{nameVacancy}</Td>
            <Td>{statusVacancy}</Td>
            <Td>{region}</Td>
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
