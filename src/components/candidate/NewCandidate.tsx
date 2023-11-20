import React from 'react'
import * as C from '../../styles/components'
import { Link } from 'react-router-dom'
import Close from '../../images/icons/Close'
import * as S from './NewCandidateStyles'

const NewCandidate = () => {
    return (
        <div>
            <S.Title>
                <C.H2>Новый кандидат</C.H2>
                <Link to="/candidates">
                    <C.NButton>
                        <C.SvgIconWrapper><Close/></C.SvgIconWrapper>
                    </C.NButton>
                </Link>
            </S.Title>
            <S.Form>
                <label htmlFor="">ФИО</label>
                <S.Input/>
                <label htmlFor="">Вакансия</label>
                <S.Select name="" id="">
                    <option value="0"></option>
                    <option value="1">Вакансия 1</option>
                    <option value="2">Вакансия 2</option>
                    <option value="3">Вакансия 3</option>
                </S.Select>
                <label htmlFor="">Телефон</label>
                <S.Input />
                <label htmlFor="">Источник</label>
                <S.Input />
                <S.RefProgramm htmlFor="">
                    <S.Checkbox type='checkbox'/>
                    Реферальная программа
                </S.RefProgramm>
                <label htmlFor="">Реферер</label>
                <S.Input />
                <label htmlFor="">Статус</label>
                <S.Select name="" id="">
                    <option value="1">Новый</option>
                    <option value="2">3-й недозвон</option>
                    <option value="3">стажировка</option>
                </S.Select>
                <label htmlFor="">Комментарии</label>
                <S.Textarea name="" id="" cols={30} rows={8}></S.Textarea>
                <C.FButton>Добавить кандидата</C.FButton>
            </S.Form>
        </div>
    )
}

export default NewCandidate
