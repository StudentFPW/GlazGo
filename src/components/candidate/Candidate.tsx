import React from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import Close from '../../images/icons/close.svg'
import * as C from '../../styles/components'
import * as S from './CandidateStyles'
import Telegram from '../../images/icons/telegram.svg'
import WatsApp from '../../images/icons/watsApp.svg'
import candidateApi from '../../services/CandidateService'
import { CANDIDATE_STATUS } from '../../config'

const Candidate = () => {
    const {id} = useParams()
    const {data: candidateData } = candidateApi.useFetchCandidateQuery(id ? id : '')
    const navigate = useNavigate()
    const handleGoBack = () => navigate(-1)
    let candidate, vacancy, recruiter
    if (candidateData) {
        candidate = candidateData.candidatId
        vacancy = candidateData.vacancyId
        recruiter = candidateData.recruterId
    }


    return (
        <div>
            <S.Title>
                <C.H2>Кандидат</C.H2>
                <C.NButton onClick={handleGoBack}>
                    <C.SvgIconWrapper><Close/></C.SvgIconWrapper>
                </C.NButton>
            </S.Title>
            <div>Прикреплен к вакансии ID рекрутером 19.11.2023</div>
            <div>
                <div>ФИО</div>
                <S.ItemValue>{candidate?.surname} {candidate?.name} {candidate?.otch}</S.ItemValue>
                <div>Вакансия</div>
                <S.ItemValue>{vacancy?.nameVacancy}</S.ItemValue>
                <div>Заказчик</div>
                <S.ItemValue></S.ItemValue>
                <div>Реферер</div>
                <S.ItemValue></S.ItemValue>
                <div>Рекрутер</div>
                <S.ItemValue>{recruiter?.lastName} {recruiter?.firstName}</S.ItemValue>
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
                    <S.Select name="" id="" value={candidateData?.statusChange}>
                        {Object.keys(CANDIDATE_STATUS).map((key) => (
                            <option value={key} key={key}>{CANDIDATE_STATUS[parseInt(key)]}</option>
                        ))}
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
