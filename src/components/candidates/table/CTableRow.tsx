import React, { FC, useState } from 'react'
import styled from 'styled-components'
import { ICandidate } from '../../../modules/ICandidate'
import { useNavigate } from 'react-router-dom'

interface CandidateItemProps {
    candidate: ICandidate
}
const CTableRow: FC<CandidateItemProps> = ({candidate}) => {
    const {candidatId, vacancyId, statusChange, recruterId, appointmentDate} = candidate

    const [showFullContent, setShowFullContent] = useState(false)

    const navigate = useNavigate()

    const handleGoToCandidate = () => {
        if (showFullContent) {
            navigate(`/candidates/${candidatId}`)
        } else {
            // Показать содержимое ячейки полностью
            setShowFullContent(true);
          }
    }

    return (
        <tr>
            <Td data-content={candidatId} onClick={handleGoToCandidate}>{candidatId}</Td>
            <Td data-content={statusChange}>{statusChange}</Td>
            <Td data-content={appointmentDate}>{appointmentDate}</Td>
        </tr>
    )
}

export default CTableRow

const Td = styled.td`
    padding: 10px 16px;
    white-space: nowrap;
    overflow: hidden;
    font-size: 14px;
    position: relative;
    &:hover {
        overflow: visible;
        &::after {
            content: attr(data-content);
            position: absolute;
            background-color: ${({ theme }) => theme.colors.lightGray};
            /* border: 1px solid ${({ theme }) => theme.colors.gray}; */
            border-radius: 4px;
            padding: 10px 16px;
            top: 0;
            left: 0;
            width: max-content;
            white-space: normal;
            z-index: 999;
        }
    }
`
