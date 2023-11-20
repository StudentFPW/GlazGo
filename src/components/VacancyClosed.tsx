import React from 'react'
import * as C from '../styles/components'
import success from '../images/success.svg'

const VacancyClosed = () => {
    return (
        <div>
            <img src={success} alt="success" />
            <C.H1>Поздравляем! Вакансия Директор закрыта</C.H1>
            <div>Вернуться к списку вакансий</div>
        </div>
    )
}

export default VacancyClosed
