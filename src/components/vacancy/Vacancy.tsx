import React, { FC, useState } from 'react'
import * as S from './VacancyStyles'
import * as C from '../../styles/components'
import Close from '../../images/icons/close.svg'
import { useNavigate, useParams } from 'react-router-dom'
import vacancyApi from '../../services/VacancyService'
import { VACANCY_STATUS } from '../../config'
import { SubmitHandler, useForm } from 'react-hook-form'
import { IVacancyChangeQueryData } from '../../modules/IVacancy'
import candidateApi from '../../services/CandidateService'
import { formatDate } from '../../utils'

const Vacancy: FC = () => {
    const {id} = useParams()
    const {data: vacancy} = vacancyApi.useFetchVacancyQuery(id ? id : '')
    const navigate = useNavigate()
    let status, customer, recruiter, date
    if (vacancy) {
        status = vacancy.statusVacancy
        customer = vacancy.customer
        recruiter = vacancy.recruter
        date = formatDate(vacancy.dateCust)
    }

    const {data} = candidateApi.useFetchVacancyAllCandidatesQuery(id ? id : '')
    const candidates = data?.results

    const handleGoToBack = () => {
        navigate(`/vacancies`)
    }
    const handleGoToCandidates = () => {
        navigate(`/vacancies/${id}/candidates`)
    }

    const {
        register,
        formState: { errors, isValid},
        handleSubmit,
        reset
    } = useForm<IVacancyChangeQueryData>({
        mode: 'onBlur',
        defaultValues: {
            salary: vacancy?.salary,
            statusVacancy: status,
        }
    })

    const onSubmit: SubmitHandler<IVacancyChangeQueryData> = async (data) => {
    // await login(data)
        setIsChange(!isChange)
    }

    const [isChange, setIsChange] = useState(false)

    const handleChange = () => {
        setIsChange(!isChange)
    }

    const handleCancel = () => {
        setIsChange(false)
        reset()
    }

    const handleCloseVacancy = () => {
        navigate(`/vacancy-closed/${id}`)
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
            </div>
            <S.Head>
                <div>
                    <p>Создана</p>
                    <p>{date}</p>
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
                <S.Select id="project" disabled={!isChange} {...register('project')}>
                    <option value="0"></option>
                    <option value="1">Проект 1</option>
                    <option value="2">Проект 2</option>
                    <option value="3">Проект 3</option>
                </S.Select>
                <label htmlFor="region">Город</label>
                <S.Select id="region" disabled={!isChange} {...register('region')}>
                    <option value="0"></option>
                    <option value="1">Город 1</option>
                    <option value="2">Город 2</option>
                    <option value="3">Город 3</option>
                </S.Select>
                <label htmlFor="salary">Зарплата</label>
                <S.Input id="salary" type="number" disabled={!isChange} {...register('salary')}/>
                <label htmlFor="schedule">График</label>
                <S.Select id="schedule" disabled={!isChange} {...register('schedule')}>
                    <option value="0"></option>
                    <option value="1">2/2</option>
                    <option value="2">5/2</option>
                    <option value="3">3/3</option>
                </S.Select>
                <label htmlFor="cause">Причина открытия вакансии</label>
                <S.Select id="cause" disabled={!isChange} {...register('cause')}>
                    <option value="0"></option>
                    <option value="1">Расширение штата</option>
                    <option value="2">Увольнение сотрудника</option>
                    <option value="3">Повышение сотрудника</option>
                </S.Select>
                <label htmlFor="link">Ссылка на вакансию</label>
                <S.Input id="link" disabled={!isChange} {...register('link')}/>
                <label htmlFor="candidate">Выбранный кандидат</label>
                <S.Select id="candidate" disabled={!isChange} {...register('candidate')}>
                    <option value="0"></option>
                    {candidates && candidates.map((candidate) => (
                        <option value={candidate.candidatId.id} key={candidate.candidatId.id}>{candidate.candidatId.surname} {candidate.candidatId.name} {candidate.candidatId.otch}</option>
                    ))}
                </S.Select>
                <label htmlFor="statusVacancy">Статус</label>
                <S.Select id="statusVacancy" disabled={!isChange} {...register('statusVacancy')}>
                    {Object.keys(VACANCY_STATUS).map((key) => (
                        <option value={key} key={key}>{VACANCY_STATUS[parseInt(key)]}</option>
                    ))}
                </S.Select>
                {isChange &&
                <S.FormButtons>
                    <C.FButton>Сохранить</C.FButton>
                    <C.FButton type="reset" onClick={handleCancel}>Отменить</C.FButton>
                </S.FormButtons>}
            </S.Form>
            <S.Buttons>
                {!isChange && <C.FButton onClick={handleChange}>Изменить вакансию</C.FButton>}
                <C.FButton onClick={handleCloseVacancy}>Закрыть вакансию</C.FButton>
                <C.LButton onClick={handleGoToCandidates}>Кандидаты</C.LButton>
                <C.LButton>Чат с рекрутером</C.LButton>
            </S.Buttons>
        </div>
    )
}

export default Vacancy
