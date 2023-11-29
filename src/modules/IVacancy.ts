import { IPagination } from "./IPagination"
import { IUser } from "./IUser"

export interface IVacancy {
    nameVacancy: string
    statusVacancy: number
    region: string
    salary: number
    id: number
    dateCust: string
    customer: IUser
    recruter: IUser
}

export interface IVacancyChangeQueryData extends IVacancy {
    project: number
    schedule: number
    cause: number
    link: string
    candidate: number
    statusVacancy: number
}

export interface IVacancyResponseData extends IPagination {
    results: IVacancy[]
}