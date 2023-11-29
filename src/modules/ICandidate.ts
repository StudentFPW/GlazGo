import { IUser } from "./IUser"
import { IVacancy } from "./IVacancy"

export interface ICandidate {
    id: number
    surname: string
    name: string
    otch: string
    email: string
    phone: string
    ref: string
    resume: string
}

export interface ICandidateProm {
    candidatId: ICandidate
    vacancyId: IVacancy
    statusChange: number
    recruterId: IUser
    appointmentDate: string
}

export interface INewCandidate extends ICandidate {
    vacancy: number
    source: string
}

