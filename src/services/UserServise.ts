import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/dist/query/react'
import { IAuthData, IAuthToken } from '../modules/IAuth'

const userApi = createApi({
    reducerPath: 'userApi',
    baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:5000'}),
    endpoints: (builder) => ({
        fetchAuth: builder.mutation<IAuthToken, IAuthData>({
            query: (authData) => ({
                url: '/auth',
                method: 'POST',
                body: authData
            })
        })
    })
})

export default userApi