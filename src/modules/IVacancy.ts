export interface IVacancy {
    nameVacancy: string
    statusVacancy: number
    region: string
    salary: number
    id: number
}

export interface IVacancyResponseData {
    results: IVacancy[]
}