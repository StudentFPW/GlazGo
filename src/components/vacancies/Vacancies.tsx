import React from 'react'
import Options from './Options'
import Pagination from './Pagination'
import * as C from '../../styles/components'
import VTable from './table/VTable'

const Vacancies = () => {
  return (
    <div>
        <C.H2>Вакансии</C.H2>
        <Options path={'/zayavka'}/>
        <VTable />
        <Pagination />
    </div>
  )
}

export default Vacancies
