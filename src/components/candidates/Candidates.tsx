import React from 'react'
import Options from '../vacancies/Options'
import Pagination from '../vacancies/Pagination'
import * as C from '../../styles/components'
import CTable from './table/CTable'
import Close from '../../images/icons/close.svg'
import { useNavigate, useParams } from 'react-router-dom'
import { styled } from 'styled-components'
import candidateApi from '../../services/CandidateService'

const Candidates = () => {
  const navigate = useNavigate()
  const handleGoToCandidates = () => {
    navigate(-1)
  }
  const {id} = useParams()
  const {data} = candidateApi.useFetchVacancyCandidatesQuery({limit: 10, id: id ? id : ''})

  return (
    <div>
      <Title>
          <C.H2>Кандидаты</C.H2>
          <C.NButton onClick={handleGoToCandidates}>
              <C.SvgIconWrapper><Close/></C.SvgIconWrapper>
          </C.NButton>
      </Title>
        <Options path={'/new-candidate'}/>
        <CTable />
        {data && <Pagination count={data.count} previous={data.previous} next={data.next} />}
    </div>
  )
}

export default Candidates

const Title = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`