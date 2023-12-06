import { FC } from 'react'
import Options from '../vacancies/Options'
import Pagination from '../vacancies/Pagination'
import * as C from '../../styles/components'
import Close from '../../images/icons/close.svg'
import { useNavigate } from 'react-router-dom'
import { styled } from 'styled-components'
import CTableAll from './table/CTableAll'

const CandidatesAll: FC = () => {
  const navigate = useNavigate()

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
        <Pagination />
    </div>
  )
}

export default CandidatesAll

const Title = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`