export interface ICandidate {
    candidatId: number
    vacancyId: number
    statusChange: number
    recruterId: number
    appointmentDate: string
    id: number
    surname: string
    name: string
    otch: string
    email: string
    phone: string
    ref: string
    resume: string
}

export interface ICandidateResponseData {
    results: ICandidate[]
}