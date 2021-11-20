import Table from '../Component/Table'
import TableHeader from '../Component/TableHeader'

const List = ({ company, location, level, tag }) => {

    return(
        <div className='list'>
            <TableHeader company={company} location={location} level={level} tag={tag} />
            <Table company={company} location={location} level={level} tag={tag}/>
        </div>
    )
}

export default List