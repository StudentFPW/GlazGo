import React from 'react'
import * as S from './ZayavkaStyled'

const Zayavka = () => {
  return (
    <S.Container>
        <S.Title>
            <p>Заявка на подбор</p>
            <p>Закрыть</p>
        </S.Title>
        <S.Head>
            <div>
                <p>Дата</p>
                <p>11.10.2023</p>
            </div>
            <div>
                <p>ID вакансии</p>
                <p>0000000011</p>
            </div>
        </S.Head>
        <S.Info>
            <div>
                <p>Заказчик:</p>
                <p>Иванов Иван Иванович</p>
            </div>
            <div>
                <p>Рекрутер:</p>
                <p>Петров Петр Петрович</p>
            </div>
            <div>
                <p>Компания:</p>
                <p>OOO "Компания"</p>
            </div>
        </S.Info>
        <S.Form>
            <label htmlFor="">Проект</label>
            <select name="" id="">
                <option value="1">Проект 1</option>
                <option value="2">Проект 2</option>
                <option value="3">Проект 3</option>
            </select>
            <label htmlFor="">Город</label>
            <select name="" id="">
                <option value="1">Город 1</option>
                <option value="2">Город 2</option>
                <option value="3">Город 3</option>
            </select>
            <label htmlFor="">Зарплата</label>
            <input type="number" />
            <label htmlFor="">График</label>
            <select name="" id="">
                <option value="1">2/2</option>
                <option value="2">5/2</option>
                <option value="3">3/3</option>
            </select>
            <label htmlFor="">Причина открытия вакансии</label>
            <select name="" id="">
                <option value="1">Расширение штата</option>
                <option value="2">Увольнение сотрудника</option>
                <option value="3">Повышение сотрудника</option>
            </select>
            <label htmlFor="">Ссылка на вакансию</label>
            <input type="text" />
        </S.Form>

    </S.Container>
  )
}

export default Zayavka
