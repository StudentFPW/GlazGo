import React from 'react'
import * as S from './ZayavkaStyles'
import * as C from '../../styles/components'
import Close from '../../images/icons/close.svg'
import { Link } from 'react-router-dom'
import { SubmitHandler, useForm } from 'react-hook-form'
import { IVacancyChangeQueryData } from '../../modules/IVacancy'

const Zayavka = () => {
    const {
        register,
        formState: { errors, isValid},
        handleSubmit
    } = useForm<IVacancyChangeQueryData>({mode: 'onBlur'})

    const onSubmit: SubmitHandler<IVacancyChangeQueryData> = async (data) => {
    // await login(data)
    }

    return (
        <div>
            <S.Title>
                <C.H2>Заявка на подбор</C.H2>
                <Link to="/vacancies">
                    <C.NButton>
                        <C.SvgIconWrapper><Close/></C.SvgIconWrapper>
                    </C.NButton>
                </Link>
            </S.Title>
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
            <S.Form onSubmit={handleSubmit(onSubmit)}>
                    <label htmlFor="project">Проект</label>
                    <S.Select id="project" {...register('project')}>
                        <option value="0"></option>
                        <option value="1">Проект 1</option>
                        <option value="2">Проект 2</option>
                        <option value="3">Проект 3</option>
                    </S.Select>
                    <label htmlFor="">Вакансия</label>
                    <S.Input />
                    <label htmlFor="region" {...register('region')}>Город</label>
                    <S.Select id="region">
                        <option value="0"></option>
                        <option value="1">Город 1</option>
                        <option value="2">Город 2</option>
                        <option value="3">Город 3</option>
                    </S.Select>
                    <label htmlFor="salary" {...register('salary')}>Зарплата</label>
                    <S.Input id="salary" type="number" {...register('salary')}/>
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

                    <C.FButton>Отправить</C.FButton>
                </S.Form>
        </div>
    )
}

export default Zayavka