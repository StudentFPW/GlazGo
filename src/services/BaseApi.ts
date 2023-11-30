import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/dist/query/react";

const baseApi = createApi({
    reducerPath: 'baseApi',
    baseQuery: fetchBaseQuery({
        baseUrl: 'http://127.0.0.1:8000',
        prepareHeaders: (headers) => {
            headers.set('Content-Type', 'application/json')
            const token = localStorage.getItem('accessToken')
            if (token) {
                headers.set('Authorization', `Bearer ${token}`)
            }
            return headers
        },
    }),
    endpoints: () => ({}),

})

export default baseApi