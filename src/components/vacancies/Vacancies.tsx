import React from 'react'
import VacanciesTable from './table/VacanciesTable'
import Options from './Options'
import Pagination from './Pagination'

const Vacancies = () => {
  return (
    <div>
        <Options/>
        <VacanciesTable />
        <Pagination />
    </div>
  )
}

export default Vacancies
