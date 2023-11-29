import React, { FC, useState } from 'react'
import * as S from './VacancyStyles'
import * as C from '../../styles/components'
import Close from '../../images/icons/close.svg'
import { useNavigate, useParams } from 'react-router-dom'
import vacancyApi from '../../services/VacancyService'
import { VACANCY_STATUS } from '../../config'
import { SubmitHandler, useForm } from 'react-hook-form'
import { IVacancyChangeQueryData } from '../../modules/IVacancy'

const Vacancy: FC = () => {
    const {id} = useParams()
    const {data: vacancy} = vacancyApi.useFetchVacancyQuery(id ? id : '')
    const navigate = useNavigate()
    let status, customer, recruiter
    if (vacancy) {
        status = vacancy.statusVacancy
        customer = vacancy.customer
        recruiter = vacancy.recruter
    }

    const handleGoToBack = () => {
        navigate(`/vacancies`)
    }
    const handleGoToCandidates = () => {
        navigate(`/vacancies/${id}/candidates`)
    }

    const {
        register,
        formState: { errors, isValid},
        handleSubmit
    } = useForm<IVacancyChangeQueryData>({mode: 'onBlur'})

    const onSubmit: SubmitHandler<IVacancyChangeQueryData> = async (data) => {
    // await login(data)
    }

    const [isChange, setIsChange] = useState(false)

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
                    <p>{customer?.lastName} {customer?.firstName}</p>
                </S.AutoItem>
                <S.AutoItem>
                    <p>Рекрутер:</p>
                    <p>{recruiter?.lastName} {recruiter?.firstName}</p>
                </S.AutoItem>
                <S.AutoItem>
                    <p>Компания:</p>
                    <p></p>
                </S.AutoItem>
            </S.Info>
            <S.Form onSubmit={handleSubmit(onSubmit)}>
                <label htmlFor="project">Проект</label>
                <S.Select id="project" {...register('project')}>
                    <option value="0"></option>
                    <option value="1">Проект 1</option>
                    <option value="2">Проект 2</option>
                    <option value="3">Проект 3</option>
                </S.Select>
                <label htmlFor="region" {...register('region')}>Город</label>
                <S.Select id="region">
                    <option value="0"></option>
                    <option value="1">Город 1</option>
                    <option value="2">Город 2</option>
                    <option value="3">Город 3</option>
                </S.Select>
                <label htmlFor="salary" {...register('salary')}>Зарплата</label>
                <S.Input id="salary" type="number" value={vacancy?.salary} {...register('salary')}/>
                <label htmlFor="schedule">График</label>
                <S.Select id="schedule" {...register('schedule')}>
                    <option value="0"></option>
                    <option value="1">2/2</option>
                    <option value="2">5/2</option>
                    <option value="3">3/3</option>
                </S.Select>
                <label htmlFor="cause">Причина открытия вакансии</label>
                <S.Select id="cause" {...register('cause')}>
                    <option value="0"></option>
                    <option value="1">Расширение штата</option>
                    <option value="2">Увольнение сотрудника</option>
                    <option value="3">Повышение сотрудника</option>
                </S.Select>
                <label htmlFor="link">Ссылка на вакансию</label>
                <S.Input id="link" {...register('link')}/>
                <label htmlFor="candidate">Выбранный кандидат</label>
                <S.Select id="candidate" {...register('candidate')}>
                    <option value="0"></option>
                    <option value="1">Кандидат 1</option>
                    <option value="2">Кандидат 2</option>
                    <option value="3">Кандидат 3</option>
                </S.Select>
                <label htmlFor="statusVacancy">Статус</label>
                <S.Select id="statusVacancy" value={status} {...register('statusVacancy')}>
                    {Object.keys(VACANCY_STATUS).map((key) => (
                        <option value={key} key={key}>{VACANCY_STATUS[parseInt(key)]}</option>
                    ))}
                </S.Select>
                <C.FButton>Сохранить</C.FButton>
            </S.Form>
            <S.Buttons>
                <C.FButton>Изменить вакансию</C.FButton>
                <C.FButton>Закрыть вакансию</C.FButton>
                <C.LButton onClick={handleGoToCandidates}>Кандидаты</C.LButton>
                <C.LButton>Чат с рекрутером</C.LButton>
            </S.Buttons>
        </div>
    )
}

export default Vacancy
