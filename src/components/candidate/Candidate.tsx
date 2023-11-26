import React from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import Close from '../../images/icons/Close'
import * as C from '../../styles/components'
import * as S from './CandidateStyles'
import Telegram from '../../images/icons/Telegram'
import WatsApp from '../../images/icons/WatsApp'
import candidateApi from '../../services/CandidateService'

const Candidate = () => {
    const {id} = useParams()
    const {data: candidate } = candidateApi.useFetchCandidateQuery(id ? id : '')
    const navigate = useNavigate()
    const handleGoBack = () => navigate(-1)

    return (
        <div>
            <S.Title>
                <C.H2>Кандидат</C.H2>
                    <C.NButton onClick={handleGoBack}>
                        <C.SvgIconWrapper><Close/></C.SvgIconWrapper>
                    </C.NButton>
            </S.Title>
            <div>Прикреплен к вакансии ID{candidate?.vacancyId} рекрутером 19.11.2023</div>
            <div>
                <div>ФИО</div>
                <S.ItemValue>{candidate?.surname} {candidate?.name} {candidate?.otch}</S.ItemValue>
                <div>Вакансия</div>
                <S.ItemValue></S.ItemValue>
                <div>Заказчик</div>
                <S.ItemValue></S.ItemValue>
                <div>Реферер</div>
                <S.ItemValue></S.ItemValue>
                <div>Рекрутер</div>
                <S.ItemValue></S.ItemValue>
                <div>Источник</div>
                <S.ItemValue></S.ItemValue>
                <div>Email</div>
                <S.ItemValue>{candidate?.email}</S.ItemValue>
                <div>Резюме</div>
                <S.ItemValue>{candidate?.resume}</S.ItemValue>
                <div>Телефон</div>
                <S.ItemValue><a href={`tel:${candidate?.phone}`}>{candidate?.phone}</a></S.ItemValue>
                <S.MessengerWrapper>
                    <a href={`https://t.me/${candidate?.phone}`}><S.Messenger><Telegram/></S.Messenger></a>
                    <a href={`https://wa.me/${candidate?.phone}`}><S.Messenger><WatsApp/></S.Messenger></a>
                </S.MessengerWrapper>
                <S.Form>
                    <label htmlFor="">Статус</label>
                    <S.Select name="" id="">
                        <option value="0"></option>
                        <option value="1">Новый</option>
                        <option value="2">3-й недозвон</option>
                        <option value="3">Стажировка</option>
                    </S.Select>
                    <label htmlFor="">Комментарии</label>
                    <S.Textarea name="" id="" cols={30} rows={8}></S.Textarea>
                    <C.FButton>Cохранить</C.FButton>
                </S.Form>
            </div>
        </div>
    )
}

export default Candidate
