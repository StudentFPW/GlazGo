import React from 'react'
import Options from '../vacancies/Options'
import Pagination from '../vacancies/Pagination'
import * as C from '../../styles/components'
import CTable from './table/CTable'

const Candidates = () => {
  return (
    <div>
        <C.H2>Кандидаты</C.H2>
        <Options path={'/new-candidate'}/>
        <CTable />
        <Pagination />
    </div>
  )
}

export default Candidates
