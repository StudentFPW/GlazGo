import React from 'react'
import Options from './Options'
import Pagination from './Pagination'
import * as C from '../../styles/components'
import VTable from './table/VTable'
import vacancyApi from '../../services/VacancyService'

const Vacancies = () => {
  const {data} = vacancyApi.useFetchVacanciesQuery(10)
  return (
    <div>
        <C.H2>Вакансии</C.H2>
        <Options path={'/zayavka'}/>
        <VTable />
        {data && <Pagination count={data.count} previous={data.previous} next={data.next} />}
    </div>
  )
}

export default Vacancies
