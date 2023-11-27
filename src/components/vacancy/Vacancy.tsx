import React, { FC } from 'react'
import * as S from '../zayavka/ZayavkaStyles'
import * as C from '../../styles/components'
import Close from '../../images/icons/close.svg'
import { useNavigate, useParams } from 'react-router-dom'
import vacancyApi from '../../services/VacancyService'
import { VACANCY_STATUS } from '../../config'

const Vacancy: FC = () => {
    const {id} = useParams()
    const {data: vacancy, isFetching, isSuccess} = vacancyApi.useFetchVacancyQuery(id ? id : '')
    const navigate = useNavigate()
    let status
    if (vacancy) status = vacancy.statusVacancy

    const handleGoToBack = () => {
        navigate(`/vacancies`)
    }
    const handleGoToCandidates = () => {
        navigate(`/vacancies/${id}/candidates`)
    }

    return (
      <div>
            <div>
                <S.Title>
                    <C.H2>Вакансия</C.H2>
                    <C.NButton onClick={handleGoToBack}>
                        <C.SvgIconWrapper><Close/></C.SvgIconWrapper>
                    </C.NButton>
                </S.Title>
                <S.VacancyName>{vacancy?.nameVacancy}</S.VacancyName>
                <S.VacancyName>{status && VACANCY_STATUS[status]}</S.VacancyName>
            </div>
            <S.Head>
                <div>
                    <p>Создана</p>
                    <p>11.10.2023</p>
                </div>
                <div>
                    <p>ID</p>
                    <p>{id}</p>
                </div>
            </S.Head>
            <S.Info>
                <S.AutoItem>
                    <p>Заказчик:</p>
                    <p></p>
                </S.AutoItem>
                <S.AutoItem>
                    <p>Рекрутер:</p>
                    <p></p>
                </S.AutoItem>
                <S.AutoItem>
                    <p>Компания:</p>
                    <p></p>
                </S.AutoItem>
            </S.Info>
            <S.Form>
                <label htmlFor="">Проект</label>
                <S.Select name="" id="">
                    <option value="0"></option>
                    <option value="1">Проект 1</option>
                    <option value="2">Проект 2</option>
                    <option value="3">Проект 3</option>
                </S.Select>
                <label htmlFor="">Город</label>
                <S.Select name="" id="">
                    <option value="0"></option>
                    <option value="1">Город 1</option>
                    <option value="2">Город 2</option>
                    <option value="3">Город 3</option>
                </S.Select>
                <label htmlFor="">Зарплата</label>
                <S.Input type="number" value={vacancy?.salary} />
                <label htmlFor="">График</label>
                <S.Select name="" id="">
                    <option value="0"></option>
                    <option value="1">2/2</option>
                    <option value="2">5/2</option>
                    <option value="3">3/3</option>
                </S.Select>
                <label htmlFor="">Причина открытия вакансии</label>
                <S.Select name="" id="">
                    <option value="0"></option>
                    <option value="1">Расширение штата</option>
                    <option value="2">Увольнение сотрудника</option>
                    <option value="3">Повышение сотрудника</option>
                </S.Select>
                <label htmlFor="">Ссылка на вакансию</label>
                <S.Input type="text" />
                <label htmlFor="">Выбранный кандидат</label>
                <S.Select name="" id="">
                    <option value="0"></option>
                    <option value="1">Кандидат 1</option>
                    <option value="2">Кандидат 2</option>
                    <option value="3">Кандидат 3</option>
                </S.Select>
                <C.FButton>Изменить вакансию</C.FButton>
            </S.Form>
            <S.Buttons>
                <C.FButton>Закрыть вакансию</C.FButton>
                <C.LButton onClick={handleGoToCandidates}>Кандидаты</C.LButton>
                <C.LButton>Чат с рекрутером</C.LButton>
            </S.Buttons>
        </div>
    )
}

export default Vacancy
