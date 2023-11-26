import camelcaseKeys from 'camelcase-keys'
import baseApi from './BaseApi'
import { ICandidate, ICandidateResponseData } from '../modules/ICandidate'

const candidateApi = baseApi.injectEndpoints({
    endpoints: (build) => ({
        fetchCandidates: build.query<ICandidateResponseData, {limit: number, id: string}>({
            query: ({limit = 10, id}) => ({
                url: `/api-c-p/?vacancy_id=${id}`,
                params: {
                    limit
                }
            }),
            transformResponse: (response: any): ICandidateResponseData => camelcaseKeys(response, { deep: true })
        }),
        fetchCandidate: build.query<ICandidate, string>({
            query: (id) => ({
                url: `/api-cand/${id}/`,
            }),
            transformResponse: (response: any): ICandidate => camelcaseKeys(response, { deep: true })
        })
    })
})

export default candidateApi