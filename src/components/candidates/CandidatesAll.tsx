import React, { FC } from 'react'
import Options from '../vacancies/Options'
import Pagination from '../vacancies/Pagination'
import * as C from '../../styles/components'
import CTable from './table/CTable'
import Close from '../../images/icons/close.svg'
import { useNavigate } from 'react-router-dom'
import { styled } from 'styled-components'
import candidateApi from '../../services/CandidateService'
import { IPagination } from '../../modules/IPagination'
import CTableAll from './table/CTableAll'

const CandidatesAll: FC = () => {
  const navigate = useNavigate()
  const {data} = candidateApi.useFetchAllCandidatesQuery()

  return (
    <div>
      <Title>
          <C.H2>Кандидаты</C.H2>
          <C.NButton onClick={() => navigate('/')}>
              <C.SvgIconWrapper><Close/></C.SvgIconWrapper>
          </C.NButton>
      </Title>
        <Options path={'/new-candidate'}/>
        <CTableAll />
        {data && <Pagination count={data.count} previous={data.previous} next={data.next} />}
    </div>
  )
}

export default CandidatesAll

const Title = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`