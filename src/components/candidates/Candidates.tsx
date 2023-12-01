import React from 'react'
import Options from '../vacancies/Options'
import Pagination from '../vacancies/Pagination'
import * as C from '../../styles/components'
import CTable from './table/CTable'
import Close from '../../images/icons/close.svg'
import { useNavigate, useParams } from 'react-router-dom'
import { styled } from 'styled-components'
import candidateApi from '../../services/CandidateService'
import vacancyApi from '../../services/VacancyService'

const Candidates = () => {
  const navigate = useNavigate()
  const {id} = useParams()
  const {data} = candidateApi.useFetchVacancyCandidatesQuery({limit: 10, id: id ? id : ''})
  const {data: vacancy} = vacancyApi.useFetchVacancyQuery(id ? id : '')

  return (
    <div>
      <Title>
          <C.H2>Кандидаты</C.H2>
          <C.NButton onClick={() => navigate(-1)}>
              <C.SvgIconWrapper><Close/></C.SvgIconWrapper>
          </C.NButton>
      </Title>
      <SubTitle>
        <div>по вакансии:</div>
        <VacancyName>{vacancy && vacancy.nameVacancy}</VacancyName>
      </SubTitle>
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
const SubTitle = styled.div`
  margin-top: -20px;
`
const VacancyName = styled.div`
  font-size: 20px;
  font-weight: 700;
  line-height: 26px; /* 130% */
  letter-spacing: -0.1px;
  margin-bottom: 30px;
`