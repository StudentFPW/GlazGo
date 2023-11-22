import React, { FC } from 'react'
import styled from 'styled-components'
import { ICandidate } from '../../../modules/ICandidate'

interface CandidateItemProps {
    candidate: ICandidate
}
const CTableRow: FC<CandidateItemProps> = ({candidate}) => {
    const {candidateName, vacancy, status, recruiter, attachmentDate, idVacancy, id} = candidate

    return (
        <tr>
            <Td data-content={candidateName}>{candidateName}</Td>
            <Td data-content={vacancy}>{vacancy}</Td>
            <Td data-content={status}>{status}</Td>
            <Td data-content={recruiter}>{recruiter}</Td>
            <Td data-content={attachmentDate}>{attachmentDate}</Td>
            <Td data-content={idVacancy}>{idVacancy}</Td>
            <Td data-content={id}>{id}</Td>
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
