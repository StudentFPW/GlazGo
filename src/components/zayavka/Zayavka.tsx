import React from 'react'
import * as S from './ZayavkaStyles'
import * as C from '../../styles/components'
import Close from '../../images/icons/Close'
import { Link } from 'react-router-dom'

const Zayavka = () => {
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
                <p>Иванов Иван Иванович</p>
            </S.AutoItem>
            <S.AutoItem>
                <p>Рекрутер:</p>
                <p>Петров Петр Петрович</p>
            </S.AutoItem>
            <S.AutoItem>
                <p>Компания:</p>
                <p>OOO "Компания"</p>
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
            <label htmlFor="">Вакансия</label>
            <S.Input />
            <label htmlFor="">Город</label>
            <S.Input />
            <label htmlFor="">Зарплата</label>
            <S.Input type="number" />
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
            <C.FButton>Отправить заявку</C.FButton>
        </S.Form>
    </div>
  )
}

export default Zayavka
