import Options from './Options'
import Pagination from './Pagination'
import * as C from '../../styles/components'
import VTable from './table/VTable'
import Close from '../../images/icons/close.svg'
import { styled } from 'styled-components'
import { useNavigate } from 'react-router-dom'

const Vacancies = () => {
  const navigate = useNavigate()
  return (
    <div>
      <Title>
          <C.H2>Вакансии</C.H2>
          <C.NButton onClick={() => navigate('/')}>
              <C.SvgIconWrapper><Close/></C.SvgIconWrapper>
          </C.NButton>
      </Title>
        <Options path={'/zayavka'}/>
        <VTable />
        <Pagination />
    </div>
  )
}

export default Vacancies

const Title = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
`