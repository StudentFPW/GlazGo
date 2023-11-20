import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/dist/query/react'
import { IAuthData, IAuthToken } from '../modules/IAuth'

const userApi = createApi({
    reducerPath: 'userApi',
    baseQuery: fetchBaseQuery({
        baseUrl: 'http://localhost:3000',
        prepareHeaders: (headers) => {
            headers.set('Content-Type', 'application/json')
            return headers
        }
    }),
    endpoints: (build) => ({
        fetchReg: build.mutation<IAuthToken, IAuthData>({
            query: (authData) => ({
                url: '/register',
                method: 'POST',
                body: JSON.stringify(authData)
            })
        }),
        fetchAuth: build.mutation<IAuthToken, IAuthData>({
            query: (authData) => ({
                url: '/login',
                method: 'POST',
                body: JSON.stringify(authData)
            })
        })
    })
})

export default userApi